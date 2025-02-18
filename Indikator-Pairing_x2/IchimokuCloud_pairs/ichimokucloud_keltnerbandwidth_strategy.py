import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
