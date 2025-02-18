import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
