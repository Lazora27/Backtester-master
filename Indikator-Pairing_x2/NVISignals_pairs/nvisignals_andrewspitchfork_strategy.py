import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
