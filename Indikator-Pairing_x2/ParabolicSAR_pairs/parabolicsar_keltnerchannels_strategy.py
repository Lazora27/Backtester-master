import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'KeltnerChannels': 1.0
        })
    )
