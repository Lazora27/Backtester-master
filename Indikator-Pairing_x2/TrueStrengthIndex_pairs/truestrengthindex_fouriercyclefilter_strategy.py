import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
