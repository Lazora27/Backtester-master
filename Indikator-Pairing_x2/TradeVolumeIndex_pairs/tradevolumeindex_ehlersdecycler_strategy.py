import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
