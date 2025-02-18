import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'TimeCycle': 1.0
        })
    )
