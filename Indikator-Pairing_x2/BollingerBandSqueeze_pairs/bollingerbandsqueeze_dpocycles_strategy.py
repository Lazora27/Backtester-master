import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'DPOCycles': 1.0
        })
    )
