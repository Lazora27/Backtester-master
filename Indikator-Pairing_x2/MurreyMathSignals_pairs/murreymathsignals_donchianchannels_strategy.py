import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'DonchianChannels': 1.0
        })
    )
