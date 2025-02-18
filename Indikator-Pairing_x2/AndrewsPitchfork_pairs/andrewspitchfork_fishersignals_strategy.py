import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'FisherSignals': 1.0
        })
    )
