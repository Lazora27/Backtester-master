import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ProjectionBands': 1.0
        })
    )
