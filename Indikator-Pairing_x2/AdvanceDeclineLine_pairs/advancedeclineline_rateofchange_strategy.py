import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und RateOfChange
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'RateOfChange': 1.0
        })
    )
