import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
