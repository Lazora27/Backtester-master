import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
