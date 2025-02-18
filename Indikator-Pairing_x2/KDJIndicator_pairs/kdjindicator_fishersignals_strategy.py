import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'FisherSignals': 1.0
        })
    )
