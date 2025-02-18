import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
