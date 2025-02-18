import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
