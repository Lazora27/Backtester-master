import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
