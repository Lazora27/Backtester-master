import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
