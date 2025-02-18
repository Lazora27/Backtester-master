import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BollingerBands
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BollingerBands': 1.0
        })
    )
