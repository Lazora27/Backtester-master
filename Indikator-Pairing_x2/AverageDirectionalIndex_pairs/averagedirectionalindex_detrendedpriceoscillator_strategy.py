import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
