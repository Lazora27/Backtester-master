import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
