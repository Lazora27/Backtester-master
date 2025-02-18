import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
