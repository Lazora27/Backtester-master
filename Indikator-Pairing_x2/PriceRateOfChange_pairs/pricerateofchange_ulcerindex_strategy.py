import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'UlcerIndex': 1.0
        })
    )
