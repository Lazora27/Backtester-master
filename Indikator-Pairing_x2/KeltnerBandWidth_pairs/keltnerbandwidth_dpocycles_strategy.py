import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und DPOCycles
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'DPOCycles': 1.0
        })
    )
