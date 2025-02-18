import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'CCITurbo': 1.0
        })
    )
