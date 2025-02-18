import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
