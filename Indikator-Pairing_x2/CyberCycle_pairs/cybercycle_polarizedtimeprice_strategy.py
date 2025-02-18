import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
