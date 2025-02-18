import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'SmoothedCycle': 1.0
        })
    )
