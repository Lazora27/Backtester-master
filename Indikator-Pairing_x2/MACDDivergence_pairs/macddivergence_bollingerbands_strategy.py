import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BollingerBands': 1.0
        })
    )
