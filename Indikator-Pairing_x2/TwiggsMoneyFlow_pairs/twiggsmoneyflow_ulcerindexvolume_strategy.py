import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwiggsMoneyFlow_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwiggsMoneyFlow und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'TwiggsMoneyFlow': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
