import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
