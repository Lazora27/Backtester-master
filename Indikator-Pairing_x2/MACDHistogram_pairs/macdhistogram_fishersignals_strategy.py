import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FisherSignals': 1.0
        })
    )
