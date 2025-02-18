import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'FisherSignals': 1.0
        })
    )
