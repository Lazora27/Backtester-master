import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'DPOCycles': 1.0
        })
    )
