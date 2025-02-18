import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'FisherSignals': 1.0
        })
    )
