import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
