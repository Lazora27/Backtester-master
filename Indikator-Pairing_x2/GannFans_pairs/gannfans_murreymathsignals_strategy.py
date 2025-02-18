import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
