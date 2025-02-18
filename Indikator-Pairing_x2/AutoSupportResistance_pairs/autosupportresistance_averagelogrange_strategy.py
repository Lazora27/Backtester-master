import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AverageLogRange': 1.0
        })
    )
