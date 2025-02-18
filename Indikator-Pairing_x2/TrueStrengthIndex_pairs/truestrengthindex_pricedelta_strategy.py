import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
