import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
