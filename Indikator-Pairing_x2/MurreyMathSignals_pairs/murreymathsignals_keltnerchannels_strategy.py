import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'KeltnerChannels': 1.0
        })
    )
