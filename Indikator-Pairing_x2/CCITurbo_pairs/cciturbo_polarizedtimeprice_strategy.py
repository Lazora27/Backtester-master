import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
