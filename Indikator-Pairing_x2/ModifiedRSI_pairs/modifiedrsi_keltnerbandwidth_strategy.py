import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
