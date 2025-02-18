import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
