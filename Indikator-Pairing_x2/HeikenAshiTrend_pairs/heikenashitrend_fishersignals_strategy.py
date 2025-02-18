import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und FisherSignals
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'FisherSignals': 1.0
        })
    )
