import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
