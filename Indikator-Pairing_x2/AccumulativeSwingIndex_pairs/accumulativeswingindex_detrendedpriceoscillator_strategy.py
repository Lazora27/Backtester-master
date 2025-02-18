import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulativeSwingIndex_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulativeSwingIndex und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'AccumulativeSwingIndex': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
