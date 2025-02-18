import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'AdaptiveATR': 1.0
        })
    )
