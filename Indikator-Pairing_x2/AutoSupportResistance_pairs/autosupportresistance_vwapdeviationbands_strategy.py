import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
