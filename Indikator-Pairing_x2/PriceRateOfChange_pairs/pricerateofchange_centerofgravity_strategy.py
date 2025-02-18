import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'CenterOfGravity': 1.0
        })
    )
