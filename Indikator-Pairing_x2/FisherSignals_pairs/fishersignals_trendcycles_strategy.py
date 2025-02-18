import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'TrendCycles': 1.0
        })
    )
