import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
