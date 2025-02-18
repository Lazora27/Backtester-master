import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
