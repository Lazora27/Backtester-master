import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
